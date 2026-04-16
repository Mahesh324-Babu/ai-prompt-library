
# AI Prompt Library

## Features
- View prompts
- View prompt details + live views
- Add prompts

## Tech Stack
- Angular
- Django
- PostgreSQL
- Redis
- Docker

## Setup
docker-compose up --build

## API
GET /prompts/
POST /prompts/
GET /prompts/:id/

## Design Decisions
- Used simple function-based views
- Redis for view counter
- Clean UI with Angular
