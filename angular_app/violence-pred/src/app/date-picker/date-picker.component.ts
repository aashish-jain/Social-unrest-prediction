import { Component } from '@angular/core';

@Component({
  selector: 'app-date-picker',
  templateUrl: './date-picker.component.html',
  styleUrls: ['./date-picker.component.css']
})
export class DatePickerComponent  {
  maxDate = new Date(2019, 4, 0);
  minDate = new Date(2016, 1, 0);
  date = new Date(2020, 1, 0);


}
