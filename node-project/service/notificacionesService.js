

function formatMessage(data,activo,tipoNotificacion,notificaciones){
   console.log(notificaciones)
   let Message=''
    if(tipoNotificacion=='fond'){
        Message += 'Fondo de inversión ACTIVITY\n-----------------------\n';
        Message += `Fondo: ${activo}\n-----------------------\n`;
        data.sort((a, b) => parseFloat(b.portfolioPart) - parseFloat(a.portfolioPart));
        let  seisMayores = data.slice(0, 6);
        seisMayores.forEach((activity) => {
            
                Message += `Activo : ${activity.name}\n`;
                Message += `Parte del portfolio: ${activity.portfolioPart}%\n`;
                Message += `Monto: ${activity.value}\n`;
                Message += `Cantidad: ${activity.cantidad} acciones\n`;
                Message += '------\n';
            })
            
            return Message

    }
    if(tipoNotificacion=='Insider'){
        let Message = 'INSIDER ACTIVITY\n-----------------------\n';
        Message += `Empresa: ${activo}\n-----------------------\n`;
        Message += `Cotizaciòn: ${parseFloat(notificaciones.Precio_int)}\n-----------------------\n`;
        data.forEach((activity) => {
            if(activity.type=="fund"){
                Message += `fondo : ${activity.operador}\n`;
                Message += `Cargo: Fondo de inversión\n`;
                Message += `Cantidad: ${activity.cantidad} acciones\n`;
                Message += `Monto: ${activity.value}\n`;
                Message += `tenencia en porfolio: ${activity.own}%\n`;
                Message += `Fecha: ${activity.fecha} \n`;
                Message += `Movimiento en porfolio: ${activity.movimiento} \n`;
    
            }
            if(activity.type=="insider"){
                Message += `Nombre: ${activity.operador}\n`;
                Message += `Cargo: ${activity.cargo}\n`;
                Message += `Cantidad: ${activity.cantidad} acciones\n`;
                Message += `Monto: ${activity.value}\n`;
                Message += `Movimiento: ${activity.own}\n`;
                Message += `Fecha: ${activity.fecha}\n`;
    
            }
            Message += '------\n';
    },
)
return Message

}
       


// Imprime el mensaje formateado

}


module.exports={
formatMessage
};