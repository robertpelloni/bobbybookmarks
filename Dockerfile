# Stage 1: Build the React/TypeScript Dual-HUD Frontend
FROM node:22-slim AS frontend-builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY index.html build-render.js tsconfig.json tsconfig.node.json vite.config.ts postcss.config.cjs tailwind.config.cjs ./
COPY src/ ./src/
RUN npm run build

# Stage 2: Build the Go Unified Backend (Pure-Go modernc.org/sqlite, CGO_ENABLED=0)
FROM golang:1.25-alpine AS backend-builder
WORKDIR /app
COPY backend/go.mod backend/go.sum ./backend/
RUN cd backend && go mod download
COPY backend/ ./backend/
RUN cd backend && CGO_ENABLED=0 GOOS=linux go build -buildvcs=false -o /bobby-backend ./cmd/api

# Stage 3: Final runtime image
FROM alpine:latest
WORKDIR /app
RUN apk add --no-cache ca-certificates

COPY --from=frontend-builder /app/dist ./dist
COPY --from=backend-builder /bobby-backend ./bobby-backend
COPY bookmarks.db ./bookmarks.db
COPY atlas.html ./atlas.html

ENV PORT=10000
EXPOSE 10000
CMD ["./bobby-backend"]
