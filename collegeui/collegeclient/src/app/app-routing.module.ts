import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {LoginComponent} from './login/app.login'
import {StudentComponent} from './student/app.student.component'

const routes: Routes = [
  {path : '', component : LoginComponent},
  {path : 'student',component: StudentComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [StudentComponent,]