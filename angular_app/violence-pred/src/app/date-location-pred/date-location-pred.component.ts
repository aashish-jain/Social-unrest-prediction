import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

export interface Result {
  probability: number;
}

@Component({
  selector: 'app-date-location-pred',
  templateUrl: './date-location-pred.component.html',
  styleUrls: ['./date-location-pred.component.css']
})
export class DateLocationPredComponent implements OnInit {

  constructor(private http: HttpClient) { }

  locationUrl = 'http://127.0.0.1:5000/locations/';
  locations : string[];

  ngOnInit() {
    this.getLocations().subscribe((data : string[]) => this.locations = data['locations']);
  }
  
  maxDate = new Date(2020, 4, 0);
  minDate = new Date(2016, 1, 0);
  date = new Date(2020, 1, 0);

  configUrl = 'http://127.0.0.1:5000/predict/';

  locationValue: string;
  dateString : string;
  result : number;
  resultString : string;
  disp : boolean;

  onClickGo() {
    this.dateString = this.date.getMonth()+1+"/"+this.date.getDate()+"/"+this.date.getFullYear();
    this.getConfig().subscribe((data : Result) => this.result = data['probability']);
    this.disp = true;
  }

  getLocations() {
    return this.http.get(this.locationUrl);
  }

  getConfig() {
    return this.http.get(this.configUrl, {params: {date: this.dateString, location: this.locationValue}});
  }


}
