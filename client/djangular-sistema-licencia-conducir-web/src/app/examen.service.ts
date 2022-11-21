import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient } from "@angular/common/http";

import { PreguntaArray } from "./examen";


//Angular dependency injection
@Injectable({
 providedIn: 'root'
})
export class ExamenService {

 constructor(private http: HttpClient) { }

 getExamen(): Observable<PreguntaArray> {
   return this.http.get('http://127.0.0.1:8000/api/v1/exam/preguntas/') as Observable<PreguntaArray>; 
  }


}