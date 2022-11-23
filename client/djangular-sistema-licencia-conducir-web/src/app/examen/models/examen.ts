export interface Opcion {
    id_opcion: number,
    descripcion: string
}
  
export interface OpcionArray extends Array<Opcion> { }

export interface OpcionDetail {
  id_opcion: number,
  descripcion: string,
  opcion_correcta: boolean
}

export interface OpcionDetailArray extends Array<OpcionDetail> { }

export interface Pregunta {
  id_pregunta: number,
  descripcion: string,
}

export interface PreguntaArray extends Array<Pregunta> { }

export interface PreguntaDetail {
  pregunta: Pregunta,
  opcion: Opcion,
  opcion_correcta: boolean;
}

export interface PreguntaDetailArray extends Array<PreguntaDetail> { }

  
