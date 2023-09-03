

function formatMessage(data,activo){
    let Message = 'INSIDER ACTIVITY\n-----------------------\n';
    Message += `Empresa: ${activo}\n-----------------------\n`;
    data.forEach((activity) => {
        if(activity.type=="fund"){
            Message += `fondo : ${activity.operador}\n`;
            Message += `Cargo: Fondo de inversión\n`;
            Message += `Cantidad: ${activity.cantidad} acciones\n`;
            Message += `Monto: ${activity.value}\n`;
            Message += `tenencia: %${activity.own} \n`;
        }
        if(activity.type=="insider"){
            Message += `Nombre: ${activity.operador}\n`;
            Message += `Cargo: ${activity.Cargo}\n`;
            Message += `Cantidad: ${activity.cantidad} acciones\n`;
            Message += `Monto: ${activity.value}\n`;
            Message += `Movimiento: ${activity.own}\n `;
        }
      
        Message += '------\n';
});

// Imprime el mensaje formateado
return Message
}

module.exports={
formatMessage
};