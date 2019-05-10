import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

export interface Result {
  lat: number;
  lon: number;
  probability: number;
}

@Component({
  selector: 'app-map-display',
  templateUrl: './map-display.component.html',
  styleUrls: ['./map-display.component.css']
})
export class MapDisplayComponent implements OnInit {

  maxDate = new Date(2019, 4, 3);
  minDate = new Date(2019, 1, 23);
  date = new Date(2019, 4, 3);
  dateString : string;
  date1String : string;
  date2String : string;
  results : Result[];
  resultString : string;
  disp : boolean;
  radiusSize : number;
  result : Result;

  constructor(private http: HttpClient) { }

  configUrl = 'http://127.0.0.1:5000/unrest-map/';

  api : string;

  lat: number = 23;
  lng: number = 82;
  zoom: number = 5;

  onClickGo() {
    this.dateString = this.date.getMonth()+1+"/"+this.date.getDate()+"/"+this.date.getFullYear();
    this.date1String = this.date.getMonth()+1+"/"+(this.date.getDate()+2)+"/"+this.date.getFullYear();
    this.date2String = this.date.getMonth()+1+"/"+(this.date.getDate()+7)+"/"+this.date.getFullYear();
    this.getConfig().subscribe((data : Result[]) => this.results = data['locations']);
    this.disp = true;
  }

  getConfig() {
    return this.http.get(this.configUrl, {params: {date: this.dateString}});
  }
  
  ngOnInit() {
  } 
  
}
