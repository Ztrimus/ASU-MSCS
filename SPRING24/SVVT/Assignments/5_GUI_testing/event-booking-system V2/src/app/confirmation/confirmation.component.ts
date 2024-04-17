// import { Component } from '@angular/core';
// import { Router } from '@angular/router';

// @Component({
//   selector: 'app-confirmation',
//   standalone: true,
//   imports: [],
//   templateUrl: './confirmation.component.html',
//   styleUrl: './confirmation.component.scss'
// })

// export class ConfirmationComponent {
//   constructor(private router: Router) {}

//   printConfirmation() {
//     window.print();
//   }

//   backToListing() {
//     this.router.navigate(['/event-listing']);
//   }
// }

// confirmation.component.ts
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-confirmation',
  templateUrl: './confirmation.component.html'
})
export class ConfirmationComponent {

  constructor(private router: Router) {}

  printConfirmation() {
    window.print();
  }

  emailDetails() {
    return
    // Implement the functionality or service to send details via email
  }

  backToListing() {
    this.router.navigate(['/event-listing']); // Make sure the route matches your event listing page
  }
}
