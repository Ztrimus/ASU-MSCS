import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ConfirmationComponent } from './confirmation.component';
import { RouterTestingModule } from '@angular/router/testing';
import { By } from '@angular/platform-browser';

describe('ConfirmationComponent', () => {
  let component: ConfirmationComponent;
  let fixture: ComponentFixture<ConfirmationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ConfirmationComponent],
      imports: [RouterTestingModule],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConfirmationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // Existence of confirmation elements
  it('should render confirmation message and buttons', () => {
    const messageElement = fixture.debugElement.query(
      By.css('h2')
    ).nativeElement;
    const paragraphElement = fixture.debugElement.query(
      By.css('p')
    ).nativeElement;
    expect(messageElement).toBeTruthy();
    expect(paragraphElement).toBeTruthy();
    expect(messageElement.textContent).toContain(
      'Thanks for Registering for the Webinar!'
    );
  });

  // Correctness of content
  it('should display correct button texts', () => {
    const printButton = fixture.debugElement.query(
      By.css('button.btn-success')
    ).nativeElement;
    const emailButton = fixture.debugElement.query(
      By.css('button.btn-primary')
    ).nativeElement;
    const backButton = fixture.debugElement.query(
      By.css('button.btn-outline-dark')
    ).nativeElement;
    expect(printButton.textContent).toContain('Print Confirmation');
    expect(emailButton.textContent).toContain('Email Details');
    expect(backButton.textContent).toContain('Back to Events');
  });

  // Correctness of buttons and actions
  it('should trigger the correct functions when buttons are clicked', () => {
    spyOn(component, 'printConfirmation');
    spyOn(component, 'emailDetails');
    spyOn(component, 'backToListing');

    const printButton = fixture.debugElement.query(
      By.css('button.btn-success')
    ).nativeElement;
    const emailButton = fixture.debugElement.query(
      By.css('button.btn-primary')
    ).nativeElement;
    const backButton = fixture.debugElement.query(
      By.css('button.btn-outline-dark')
    ).nativeElement;

    printButton.click();
    emailButton.click();
    backButton.click();

    expect(component.printConfirmation).toHaveBeenCalled();
    expect(component.emailDetails).toHaveBeenCalled();
    expect(component.backToListing).toHaveBeenCalled();
  });

  // Styling and layout
  it('should have correctly styled buttons', () => {
    const printButton = fixture.debugElement.query(
      By.css('button.btn-success')
    );
    const backButton = fixture.debugElement.query(
      By.css('button.btn-outline-dark')
    );
    expect(printButton).toBeTruthy();
    expect(backButton.classes['ms-2']).toBeTruthy(); // Verify that margin spacing class is applied
  });

  // Navigation and link correctness
  it('should navigate to the correct route when back button is clicked', () => {
    const router = TestBed.inject(Router);
    const navigateSpy = spyOn(router, 'navigate');

    const backButton = fixture.debugElement.query(
      By.css('button.btn-outline-dark')
    ).nativeElement;
    backButton.click();
    expect(navigateSpy).toHaveBeenCalledWith(['events']); // Adjust as per the actual route
  });
});
