import { Component, OnInit } from '@angular/core';
import {  ElementRef, HostListener, ViewChild } from '@angular/core';
import { StocksService } from 'src/app/services/stocks.service';
import { miLista } from 'src/app/data/stocks';
import { ActivatedRoute,Params } from '@angular/router';

@Component({
  selector: 'app-selector-assets',
  templateUrl: './selector-assets.component.html',
  styleUrls: ['./selector-assets.component.css']
})
export class SelectorAssetsComponent implements OnInit {
  @ViewChild('scrollContainer') scrollContainer!: ElementRef;

  constructor(private tuServicio: StocksService,
    private route: ActivatedRoute) { }
  data: any=[]
  toBeDisplay:any=[]
  slicer:number=1
  selectedIdStocks:any=[]
  selectedStocks:any=[]
  valorNombre:any
  id: string;
  loading:boolean=false
  errores:number=0


  ngOnInit(): void {
    this.route.queryParams.subscribe((params: Params) => {
      // Obtener el valor de la variable 'key' de la URL
      const key = params['key'];

      // Hacer algo con el valor de 'key'
      console.log('Valor de key:', key);
      if(key){
        this.id = key;
      }
      else{
        this.id = "0"
      }
    });


    console.log(this.id)


    miLista.reverse()
    miLista.forEach(x=>{this.data.push(x)
       })
    this.toBeDisplay=this.data.slice(0, 50)


    this.tuServicio.getUserAssets(this.id).subscribe(
      (result) => {
        result;
        if(result.statusCode!=0){
          this.filtrarPorWebID( result.mensaje)

        }
      },
      (error) => {
        console.error('Error:', error);
      }
    );
  }

  handleImageError(event: Event, item: any): void {
    // Cambia la fuente de la imagen a una imagen gris o a otra imagen alternativa
    const imgElement = event.target as HTMLImageElement;
    imgElement.src = 'assets/gris.avif'; // Reemplaza con la ruta de tu imagen gris o alternativa
  }

  selected(item: any){
    const imgElement = event.target as HTMLImageElement;
    //imgElement.style.backgroundColor= "gainsboro";
    console.log(item)
    if(this.selectedIdStocks.indexOf(item.webID)>=0){
      this.selectedIdStocks =  this.selectedIdStocks.filter(numero => numero !== item.webID);
      this.selectedStocks=  this.selectedStocks.filter(numero => numero.webID !== item.webID);
    }
    else{
      this.selectedIdStocks.push(item.webID)
      this.selectedStocks.push(item)
    }
    console.log(this.selectedIdStocks)
  }

  verMas(){
  this.slicer=this.slicer+1

  this.toBeDisplay=this.data.slice(0,50*this.slicer)
  }

  enviar(){
    this.loading=true

    this.tuServicio.cargarAssets(this.selectedStocks,this.id).subscribe(data =>{
      if(data.statusCode =="200"){
        this.loading=false
        this.errores=1
      }
      else{
        this.errores=2

      }
    })
    }

  cambio(miInput:string){

    console.log(this.filtrarPorLetra(miInput))
    this.toBeDisplay=this.filtrarPorLetra(miInput).slice(0,200)
    if(miInput.length<=1){
      this.toBeDisplay=this.data.slice(0,50*this.slicer)

    }
  }

   filtrarPorLetra(letra) {
    const letraMayuscula = letra.toUpperCase();

    const resultadosFiltrados = this.data.filter(stock => {
      const nombreMayuscula = stock.displayName.toUpperCase();
      const activoMayuscula = stock.asset.toUpperCase();

      return nombreMayuscula.startsWith(letraMayuscula) || activoMayuscula.startsWith(letraMayuscula);
    });

    return resultadosFiltrados;
  }
   filtrarPorWebID( webIDs:[]) {
    console.log(webIDs)
    webIDs.forEach(webid =>{
      let datafilter=(this.data.filter(objeto => objeto.webID == webid)[0])
      this.selectedIdStocks.push(parseInt(webid))
     this.selectedStocks.push(datafilter)
    })
    console.log(this.selectedIdStocks)

  }
}
