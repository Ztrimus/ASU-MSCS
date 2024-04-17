import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from '../material.module';
import { EventRegistrationComponent } from './event-registration.component';



@NgModule({
  declarations: [
    EventRegistrationComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    MaterialModule,
  ]
})
export class EventRegistrationModule { }
