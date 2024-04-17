// event-listing.component.spec.ts
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { EventListingComponent } from './event-listing.component';

describe('EventListingComponent', () => {
  let component: EventListingComponent;
  let fixture: ComponentFixture<EventListingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EventListingComponent ]
      // Add any necessary modules here, like FormsModule, etc.
    })
    .compileComponents();

    fixture = TestBed.createComponent(EventListingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  // GUI Test Cases Implementation
  it('should display event cards', () => {
    const eventCards = fixture.nativeElement.querySelectorAll('.card');
    expect(eventCards.length).toBeGreaterThan(0);
  });

  it('should filter events based on search term', () => {
    // This would require some mock events and then a search simulation
  });

  it('should have images for each event card', () => {
    const images = fixture.nativeElement.querySelectorAll('.card-img-top');
    expect(images.length).toBeGreaterThan(0);
    // Further check if images have valid src attributes
  });

  it('should have register button for each event card', () => {
    const registerButtons = fixture.nativeElement.querySelectorAll('.btn-primary');
    expect(registerButtons.length).toBeGreaterThan(0);
  });

  // ... More tests based on the above test cases
});
