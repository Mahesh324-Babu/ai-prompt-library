import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class ApiService {
  baseUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  getPrompts() {
    return this.http.get(`${this.baseUrl}/prompts/`);
  }

  getPrompt(id: number) {
    return this.http.get(`${this.baseUrl}/prompts/${id}/`);
  }

  addPrompt(data: any) {
    return this.http.post(`${this.baseUrl}/prompts/`, data);
  }
}
