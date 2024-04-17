import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from '../material.module';
import { EventListingComponent } from './event-listing.component';

@NgModule({
  declarations: [
    EventListingComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    MaterialModule,
  ]
})
export class EventListingModule { }
