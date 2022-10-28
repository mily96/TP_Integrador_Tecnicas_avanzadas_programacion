import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
//My components
import { ExamenComponent } from "./examen/examen.component";

const routes: Routes = [
  { path: '', component: ExamenComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
