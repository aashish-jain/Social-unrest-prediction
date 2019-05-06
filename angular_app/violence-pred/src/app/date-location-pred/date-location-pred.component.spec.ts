import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DateLocationPredComponent } from './date-location-pred.component';

describe('DatePickerComponent', () => {
  let component: DateLocationPredComponent;
  let fixture: ComponentFixture<DateLocationPredComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DateLocationPredComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DateLocationPredComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
