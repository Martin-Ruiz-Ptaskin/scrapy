import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SelectorAssetsComponent } from './commons/selector-assets/selector-assets.component';

const routes: Routes = [
  //{ path: '',  redirectTo: '/selector', pathMatch: 'full' },

  { path: '', component: SelectorAssetsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
