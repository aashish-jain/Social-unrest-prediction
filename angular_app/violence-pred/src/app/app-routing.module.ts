import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DateLocationPredComponent }   from './date-location-pred/date-location-pred.component';
import { MapDisplayComponent }      from './map-display/map-display.component';

const routes: Routes = [
  { path: '', redirectTo: '/unrest-map', pathMatch: 'full' },
  { path: 'unrest-map', component: MapDisplayComponent },
  { path: 'date-location-prediction', component: DateLocationPredComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
