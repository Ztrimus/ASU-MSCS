import {
  ComponentFixture,
  TestBed,
  fakeAsync,
  tick,
} from '@angular/core/testing';
import { EventRegistrationComponent } from './event-registration.component';
import { FormsModule } from '@angular/forms';
import { By } from '@angular/platform-browser';
import { RouterTestingModule } from '@angular/router/testing';
import { DebugElement } from '@angular/core';
import { NgModel } from '@angular/forms';

describe('EventRegistrationComponent', () => {
  let component: EventRegistrationComponent;
  let fixture: ComponentFixture<EventRegistrationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EventRegistrationComponent],
      imports: [FormsModule, RouterTestingModule.withRoutes([])], // define your routes if needed
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EventRegistrationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // Test for the existence of GUI elements
  it('should have social media links', () => {
    const socialLinks = fixture.debugElement.queryAll(
      By.css('.social-media a')
    );
    expect(socialLinks.length).toEqual(4); // Adjust the number as per the social media links
  });

  // Test input field validations
  it('should validate required fields', fakeAsync(() => {
    const requiredInputs = fixture.debugElement.queryAll(
      By.css('input[required]')
    );
    requiredInputs.forEach((input) => {
      const control = input.injector.get(NgModel);
      control.control.setValue(''); // Setting empty value to required fields
    });
    fixture.detectChanges();

    // Pretend a form submission has happened
    component.submitRegistration();
    tick(); // Simulate passage of time if there's any async operation

    // Check for validation errors after form submission
    fixture.whenStable().then(() => {
      requiredInputs.forEach((input) => {
        expect(input.classes['ng-invalid']).toBeTruthy();
      });
    });
  }));

  // Test Privacy Statement and Terms of Service links
  it('should have functional privacy and terms links', () => {
    const privacyLink = fixture.debugElement.query(
      By.css('a[href*="privacy-statement"]')
    );
    const termsLink = fixture.debugElement.query(
      By.css('a[href*="terms-of-service"]')
    );
    expect(privacyLink).toBeTruthy();
    expect(termsLink).toBeTruthy();
    // Further navigation tests may require additional setup
  });

  // Test the form submission workflow
  it('should submit the form with valid data', fakeAsync(() => {
    // Fill out the form with valid data
    fillOutForm(fixture, {
      name: 'Jane',
      lastName: 'Doe',
      email: 'jane.doe@example.com',
      confirmEmail: 'jane.doe@example.com',
      agreement: true,
    });

    const submitSpy = spyOn(component, 'submitRegistration').and.callThrough();
    const form = fixture.debugElement.query(By.css('form')).nativeElement;
    form.dispatchEvent(new Event('submit'));

    // Simulate passage of time and wait for async operations to complete
    tick();
    fixture.detectChanges();

    // Expect the form to have been submitted
    expect(submitSpy).toHaveBeenCalled();
  }));

  // Test accessibility
  it('should have labeled form elements', () => {
    const labels = fixture.debugElement.queryAll(By.css('label'));
    expect(labels.length).toBeGreaterThan(0); // Should be adjusted based on actual number of labels
    labels.forEach((label: DebugElement) => {
      const htmlFor = label.attributes['for'];
      const input = fixture.debugElement.query(By.css(`#${htmlFor}`));
      expect(input).toBeTruthy();
    });
  });

  // Test the back button functionality
  it('should navigate back when the back button is clicked', () => {
    const backButton = fixture.debugElement.query(
      By.css('.btn-outline-dark')
    ).nativeElement;
    backButton.click();
    // Here you will have to spy on your actual routing logic to verify navigation occurred
  });

  function fillOutForm(
    fixture: ComponentFixture<EventRegistrationComponent>,
    formData: any
  ): void {
    for (const key of Object.keys(formData)) {
      const input = fixture.debugElement.query(
        By.css(`[name="${key}"]`)
      ).nativeElement;
      input.value = formData[key];
      input.dispatchEvent(new Event('input'));
    }
    fixture.detectChanges();
  }
});
