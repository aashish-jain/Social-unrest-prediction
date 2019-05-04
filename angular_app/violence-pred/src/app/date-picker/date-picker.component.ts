import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

export interface Location {
  value: string;
  viewValue: string;
}

export interface Result {
  probability: number;
}

@Component({
  selector: 'app-date-picker',
  templateUrl: './date-picker.component.html',
  styleUrls: ['./date-picker.component.css']
})
export class DatePickerComponent  {

  constructor(private http: HttpClient) { }
  
  maxDate = new Date(2020, 4, 0);
  minDate = new Date(2016, 1, 0);
  date = new Date(2020, 1, 0);

  configUrl = 'http://127.0.0.1:5000/';
  locationValue: string;
  dateString : string;
  result : number;
  resultString : string;
  disp : boolean;
  
  locations: Location[] = [
    {value: 'Delhi', viewValue: 'Delhi'},
    {value: 'Chennai', viewValue: 'Chennai'},
    {value: 'Bangalore', viewValue: 'Bangalore'}
  ];

  onClickGo() {
    this.dateString = this.date.getMonth()+1+"/"+this.date.getDate()+"/"+this.date.getFullYear();
    this.getConfig().subscribe((data : Result) => this.result = data['probability']);
    this.disp = true;
  }

  getConfig() {
    return this.http.get(this.configUrl, {params: {date: this.dateString, location: this.locationValue}});
  }


}
