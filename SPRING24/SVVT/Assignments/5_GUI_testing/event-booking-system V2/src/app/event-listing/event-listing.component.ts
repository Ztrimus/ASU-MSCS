// event-listing.component.ts
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AppService } from '../app.service';

@Component({
  selector: 'app-event-listing',
  templateUrl: './event-listing.component.html',
  styleUrls: ['./event-listing.component.scss']
})
export class EventListingComponent {
  searchTerm: string = '';
  events = this.getRandomEvents(this.appService.events, 9);

  constructor(private router: Router, public appService: AppService) {
    this.initializeEvents();
  }

  initializeEvents() {
    this.events.forEach(event => {
      // Generate random image ID between 1 and 1000
      const imageId = Math.floor(Math.random() * 1000) + 1;
      // Generate random attendee number between 10 and 100
      const attendees = Math.floor(Math.random() * 90) + 10;
      // Set the image URL using the generated image ID
      event.image = `https://picsum.photos/200/300?random=${imageId}`;
      event.attendees = attendees;
    });
  }

  navigateToRegistration(eventId: number) {
    this.router.navigate(['/event-registration', { id: eventId }]);
  }

  getRandomEvents(eventsList: any, numEvents: any) {
    let shuffled = [...eventsList].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, numEvents);
  }
}
