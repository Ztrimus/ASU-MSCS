import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AppService } from '../app.service';

@Component({
  selector: 'app-event-registration',
  templateUrl: './event-registration.component.html',
  styleUrls: ['./event-registration.component.scss'] // Corrected property name
})


export class EventRegistrationComponent {
  event_id: number = 0;
  registration = {
    name: '',
    lastName: '',
    email: '',
    confirmEmail: '',
    address: '',
    city: '',
    topic: 'Join Test Webinar', // Assuming this is static for the form
    description: 'Deneme yapmıyorum', // Static description
    time: 'Jan 4, 2021 01:00 PM in Istanbul', // Static time
    agreement: false // To track if the user agreed to terms and conditions
  };

  eventImage: string = 'path/to/default-event-image.jpg';

  constructor(private route: ActivatedRoute, private router: Router, public appService: AppService) {
    this.route.params.subscribe(params => {
      this.event_id = params['id']-1;
      this.registration.topic = this.appService.events[this.event_id].title;
      this.registration.description = this.appService.events[this.event_id].description;
      this.registration.time = this.appService.events[this.event_id].date.toDateString();

    });
  }

  submitRegistration() {
    // Implementation for submitting the registration
    this.router.navigate(['/confirmation']);
  }

  backToListing() {
    this.router.navigate(['/event-listing']);
  }
}
