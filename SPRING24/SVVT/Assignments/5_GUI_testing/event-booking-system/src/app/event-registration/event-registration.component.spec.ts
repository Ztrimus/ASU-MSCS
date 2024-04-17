import { ComponentFixture, TestBed } from '@angular/core/testing';
import { EventRegistrationComponent } from './event-registration.component';
import { FormsModule } from '@angular/forms';
import { By } from '@angular/platform-browser';
import { RouterTestingModule } from '@angular/router/testing';

describe('EventRegistrationComponent', () => {
  let component: EventRegistrationComponent;
  let fixture: ComponentFixture<EventRegistrationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EventRegistrationComponent],
      imports: [FormsModule, RouterTestingModule],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EventRegistrationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // Test for the existence of GUI elements
  it('should have all required form inputs', () => {
    expect(fixture.debugElement.query(By.css('#name'))).toBeTruthy();
    expect(fixture.debugElement.query(By.css('#email'))).toBeTruthy();
    expect(fixture.debugElement.query(By.css('#agreement'))).toBeTruthy();
    expect(
      fixture.debugElement.query(By.css('button[type="submit"]'))
    ).toBeTruthy();
    expect(
      fixture.debugElement.queryAll(By.css('.form-control')).length
    ).toBeGreaterThan(5); // Number based on visible inputs
  });

  // Test for content correctness in GUI elements
  it('should display correct topic and description', () => {
    fixture.detectChanges();
    const topicInput = fixture.debugElement.query(
      By.css('input[readonly][name="topic"]')
    ).nativeElement;
    const descriptionTextarea = fixture.debugElement.query(
      By.css('textarea[readonly][name="description"]')
    ).nativeElement;
    expect(topicInput.value).toContain('Join Test Webinar');
    expect(descriptionTextarea.value).toContain('Deneeme yapmıyorum');
  });

  // Test navigation links
  it('should navigate back on clicking the back button', () => {
    const router = TestBed.inject(Router);
    const navigateSpy = spyOn(router, 'navigate');

    const backButton = fixture.debugElement.query(
      By.css('button.btn-outline-dark')
    ).nativeElement;
    backButton.click();
    expect(navigateSpy).toHaveBeenCalledWith(['']); // Adjust as per actual navigation route
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
