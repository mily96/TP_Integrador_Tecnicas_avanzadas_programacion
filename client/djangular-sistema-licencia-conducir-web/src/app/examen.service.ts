import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient } from "@angular/common/http";

import { QuestionArray } from "./examen";

//Angular dependency injection
@Injectable({
 providedIn: 'root'
})
export class ExamenService {

 constructor(private http: HttpClient) { }

 getExamen(): Observable<QuestionArray> {
   return this.http.get('http://127.0.0.1:8000/api/v1/questions/') as Observable<QuestionArray>;
 }
}