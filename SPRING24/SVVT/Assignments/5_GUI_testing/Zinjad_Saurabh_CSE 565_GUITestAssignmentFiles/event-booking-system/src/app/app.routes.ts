import { Routes } from '@angular/router';
import { EventListingComponent } from './event-listing/event-listing.component';
import { EventRegistrationComponent } from './event-registration/event-registration.component';
import { ConfirmationComponent } from './confirmation/confirmation.component';

export const routes: Routes = [
  { path: '', redirectTo: '/event-listing', pathMatch: 'full' },
  { path: 'event-listing', component: EventListingComponent },
  { path: 'event-registration', component: EventRegistrationComponent },
  { path: 'confirmation', component: ConfirmationComponent }
];
