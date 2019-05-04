
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatDatepickerModule, MatInputModule,MatNativeDateModule} from '@angular/material';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { DatePickerComponent } from './date-picker/date-picker.component';
import { HttpClientModule }    from '@angular/common/http';
import {MatSelectModule} from '@angular/material/select';
import {MatButtonModule} from '@angular/material/button';


@NgModule({
   declarations: [
      AppComponent,
      DatePickerComponent
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
      MatButtonModule
   ],
   providers: [],
   bootstrap: [AppComponent]
})
export class AppModule { }