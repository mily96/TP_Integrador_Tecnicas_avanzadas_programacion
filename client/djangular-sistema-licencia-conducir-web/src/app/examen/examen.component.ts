import { Component, OnInit } from '@angular/core';
import { ExamenService } from "./services/examen.service";
import { Pregunta, PreguntaDetailArray, Opcion, OpcionDetailArray, OpcionDetail, PreguntaDetail} from "./models/examen";
import { MatRadioChange } from "@angular/material/radio";

@Component({
  selector: 'app-examen',
  templateUrl: './examen.component.html',
  styleUrls: ['./examen.component.scss']
})
export class ExamenComponent implements OnInit {
  examenData: PreguntaDetailArray = [];
  question: Pregunta|null = null;
  option: OpcionDetail|null = null;
  options: OpcionDetailArray = [];
  disableRadioButtons: boolean = false;
  disableNextButton: boolean = true;
  questionNumber: number = 1;
  correctAnswers: number = 0;
  constructor(private examenService: ExamenService) { }

  ngOnInit(): void {
    this.getExamen();
  }

  getExamen() {
    this.examenService.getExamen().subscribe({
        next: (data) => {
          this.examenData = data.map((x: any) => {
            const preguntaDetail: PreguntaDetail = {
              pregunta: x.id_pregunta,
              opcion: x.id_opcion,
              opcion_correcta: x.opcion_correcta
            };
            return preguntaDetail;
          });
          this.getNextQuestion();
        },
        error: (error) => {
          console.log(error);
        }
      }
    )
  }

  getNextQuestion() {
    this.options = [];
    if (this.examenData.length) {
      const index = Math.floor(Math.random() * this.examenData.length);
      this.question = this.examenData[index].pregunta;
    } else {
      this.question = null;
    }
    if (this.question) {
      this.examenData.forEach(preguntaDetail => {
        if (preguntaDetail.pregunta.id_pregunta == this.question?.id_pregunta) {
          const optionDetail: OpcionDetail = {
            id_opcion: preguntaDetail.opcion.id_opcion,
            descripcion: preguntaDetail.opcion.descripcion,
            opcion_correcta: preguntaDetail.opcion_correcta
          };
          this.options?.push(optionDetail)
        }
      });
      console.log(this.options);
      const examDataWithoutQuestion: PreguntaDetailArray = [];
      this.examenData.forEach(preguntaDetail => {
        if (preguntaDetail.pregunta.id_pregunta != this.question?.id_pregunta) {
          examDataWithoutQuestion.push(preguntaDetail);
        }
      });
      this.examenData = examDataWithoutQuestion;
    }
    if (this.option) {
      if (this.questionNumber < 10) {
        this.questionNumber++;
      }
      if (this.option.opcion_correcta) {
        this.correctAnswers++;
      }
    }
    this.option = null;
    this.disableRadioButtons = false;
    this.disableNextButton = true; 
  }

  getCorrectOption() {
    let opcion_correcta = '';
    if (this.question) {
      this.options.forEach(option => {
        if (option.opcion_correcta) {
          opcion_correcta = option.descripcion;
        }
      });
    }
    return opcion_correcta;
  }

  optionSelected(event: MatRadioChange) {
    this.disableRadioButtons = true;
    this.disableNextButton = false;
  }

}
