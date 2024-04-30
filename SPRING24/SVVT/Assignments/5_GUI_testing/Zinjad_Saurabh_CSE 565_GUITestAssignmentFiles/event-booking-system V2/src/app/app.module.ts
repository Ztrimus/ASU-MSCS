import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from './material.module';
import { EventListingModule } from './event-listing/event-listing.module';
import { EventRegistrationModule } from './event-registration/event-registration.module';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    MaterialModule,
    EventListingModule,
    EventRegistrationModule,
  ],
  declarations: [
  ],
  providers: [],
  bootstrap: [],
})
export class AppModule { }
