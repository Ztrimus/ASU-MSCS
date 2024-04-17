// event-listing.component.spec.ts
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { EventListingComponent } from './event-listing.component';

describe('EventListingComponent', () => {
  let component: EventListingComponent;
  let fixture: ComponentFixture<EventListingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EventListingComponent],
      imports: [EventListingModule],
    }).compileComponents();

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
    const registerButtons =
      fixture.nativeElement.querySelectorAll('.btn-primary');
    expect(registerButtons.length).toBeGreaterThan(0);
  });

  // Test for correctness of content
  it('should bind title and description correctly to each card', () => {
    component.events = [
      {
        id: 1,
        title: 'Test Event',
        description: 'This is a test event',
        image: 'test.jpg',
        attendees: 10,
        date: new Date(),
      },
    ]; // Mock data
    fixture.detectChanges();
    const title = fixture.debugElement.query(By.css('.card-title'))
      .nativeElement.innerText;
    const description = fixture.debugElement.query(By.css('.card-text'))
      .nativeElement.innerText;
    expect(title).toContain('Test Event');
    expect(description).toContain('This is a test event');
  });

  // Test for existence of GUI elements
  it('should have an input box for searching events', () => {
    const inputBox = fixture.debugElement.query(By.css('.form-control'));
    expect(inputBox).toBeTruthy();
  });

  // Test for the size of the event images
  it('should have images with correct height', () => {
    component.events = [
      {
        id: 1,
        title: 'Test Event',
        description: 'This is a test event',
        image: 'test.jpg',
        attendees: 10,
        date: new Date(),
      },
    ]; // Mock data
    fixture.detectChanges();
    const img = fixture.debugElement.query(
      By.css('.card-img-top')
    ).nativeElement;
    expect(img.style.height).toEqual('150px');
  });

  // Test for navigation correctness on clicking 'Register'
  it('should navigate to registration page on clicking "Register"', () => {
    component.events = [
      {
        id: 1,
        title: 'Test Event',
        description: 'This is a test event',
        image: 'test.jpg',
        attendees: 10,
        date: new Date(),
      },
    ]; // Mock data
    fixture.detectChanges();
    const router = TestBed.inject(Router); // Import and inject Angular Router
    const navigateSpy = spyOn(router, 'navigate');

    const registerButton = fixture.debugElement.query(
      By.css('.btn-primary')
    ).nativeElement;
    registerButton.click();
    expect(navigateSpy).toHaveBeenCalledWith([
      'register',
      component.events[0].id,
    ]);
  });

  // Test for 'Details' button functionality
  it('should perform the correct action on clicking "Details"', () => {
    // Assume 'Details' button should log to console as a stand-in for actual functionality
    component.events = [
      {
        id: 1,
        title: 'Test Event',
        description: 'This is a test event',
        image: 'test.jpg',
        attendees: 10,
        date: new Date(),
      },
    ]; // Mock data
    fixture.detectChanges();
    spyOn(console, 'log'); // Mock console.log if it's used for the action

    const detailsButton = fixture.debugElement.query(
      By.css('.btn-outline-secondary')
    ).nativeElement;
    detailsButton.click();
    expect(console.log).toHaveBeenCalled(); // Replace with actual functionality tests
  });
});
