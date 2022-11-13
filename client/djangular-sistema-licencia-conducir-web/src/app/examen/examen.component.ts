import { Component, OnInit } from '@angular/core';
import { ExamenService } from "../examen.service";
import { Question, QuestionArray, Answer} from "../examen";
import { MatRadioChange } from "@angular/material/radio";

@Component({
  selector: 'app-examen',
  templateUrl: './examen.component.html',
  styleUrls: ['./examen.component.scss']
})
export class ExamenComponent implements OnInit {
  examenData: QuestionArray = [];
  question: Question|null = null;
  answer: Answer|null = null;
  disableRadioButtons: boolean = false;
  disableNextButton: boolean = true;
  questionNumber: number = 0;
  correctAnswers: number = 0;
  constructor(private examenService: ExamenService) { }

  ngOnInit(): void {
    this.getExamen();
  }

  getExamen() {
    this.examenService.getExamen().subscribe({
        next: (data) => {
          this.examenData = data;
          this.getNextQuestion();
        },
        error: (error) => {
          console.log(error);
        }
      }
    )
  }

  getNextQuestion() {
    if (this.examenData.length) {
      const index = Math.floor(Math.random() * this.examenData.length);
      this.question = this.examenData[index];
      this.examenData.splice(index, 1);
    } else {
      this.question = null;
    }
    if (this.answer) {
      this.questionNumber++;
      if (this.answer.is_correct) {
        this.correctAnswers++;
      }
    }
    this.answer = null;
    this.disableRadioButtons = false;
    this.disableNextButton = true; 
  }

  getCorrectAnswer() {
    if (this.question) {
      return this.question.answers.filter(answer => answer.is_correct)[0].answer;
    }
    return '';
  }

  answerSelected(event: MatRadioChange) {
    this.disableRadioButtons = true;
    this.disableNextButton = false;
  }

}
