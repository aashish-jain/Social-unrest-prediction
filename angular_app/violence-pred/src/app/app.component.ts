import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  title = 'Election Violence and Social Unrest Prediction';
  links = [{path: 'unrest-map', label: 'Unrest Map'}, {path: 'date-location-prediction', label: 'Location-wise Prediction'}]; 
  activeLink

  ngOnInit() {
    this.activeLink = this.links[0];
  }


}

