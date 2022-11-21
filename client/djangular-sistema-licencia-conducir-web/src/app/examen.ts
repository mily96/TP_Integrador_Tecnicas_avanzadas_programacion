import * as internal from "stream";

export interface Opcion {
    id_opcion: number,
    descripcion: string,
    opcion_correcta: boolean;
  }
  
interface OpcionArray extends Array<Opcion> { }

export interface Pregunta {
  id_pregunta: number,
  descripcion: string,
}

export interface PreguntaArray extends Array<Pregunta> { }

  
