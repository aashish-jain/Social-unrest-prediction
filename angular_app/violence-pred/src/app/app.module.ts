
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatDatepickerModule, MatInputModule,MatNativeDateModule} from '@angular/material';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { DateLocationPredComponent } from './date-location-pred/date-location-pred.component';
import { HttpClientModule }    from '@angular/common/http';
import {MatSelectModule} from '@angular/material/select';
import {MatButtonModule} from '@angular/material/button';
import { MapDisplayComponent } from './map-display/map-display.component';
import { AgmCoreModule } from '@agm/core';
import {MatTabsModule} from '@angular/material/tabs';



@NgModule({
   declarations: [
      AppComponent,
      DateLocationPredComponent,
      MapDisplayComponent
   ],
   imports: [
      BrowserModule,
      BrowserAnimationsModule,
      MatDatepickerModule, MatInputModule,MatNativeDateModule,
      FormsModule,
      ReactiveFormsModule,
      AppRoutingModule,
      HttpClientModule,
      MatSelectModule,
      MatButtonModule,
      MatTabsModule,
      AgmCoreModule.forRoot({
         apiKey: 'AIzaSyAD67KEh1g_dUA9OVzHP7h1NvQPbRy5n4w'
       })
   ],
   providers: [],
   bootstrap: [AppComponent]
})
export class AppModule { }