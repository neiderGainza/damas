function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
    // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}




const lista_jugadores  = document.querySelector("#lista_jugadores")
const formulario       = document.querySelector('#main_jugadores-search')
const busqueda         = document.querySelector('#buscar')
const cancelar_busqueda= document.querySelector('#cancelar_buscar')


const crear_cabecera = ()=>{
    let li_cabecera =  document.createElement('li');
    let span_cabecera = document.createElement('span')
    let span_cabecera1 = document.createElement('span')
   
    span_cabecera.innerText = 'Nombre';
    span_cabecera1.innerText = 'Seguir';
   
    li_cabecera.style.backgroundColor = "gray";

    li_cabecera.appendChild(span_cabecera)
    li_cabecera.appendChild(span_cabecera1)

    return li_cabecera
}


const crear_jugador = (name,val) =>{
    let lic     = document.createElement('li')
    let nombrec = document.createElement('span')
    let spanc   = document.createElement('span')
    let togglec = document.createElement('form')
    let inputc  = document.createElement('input')

    togglec.classList.add("main_jugadores-item-toggle")
    togglec.action = "#"
    togglec.method = "post"
    inputc.type = "checkbox";
    if (val){ inputc.click() }

    togglec.appendChild(inputc)
    togglec.appendChild(spanc)


    nombrec.innerText = name
    lic.appendChild(nombrec)
    lic.appendChild(togglec)


    spanc.addEventListener("click", ()=>{ inputc.click();})
    
    inputc.addEventListener('change', async ()=>{
        let urlServer = "http://127.0.0.1:8000/";
        let csrftoken = getCookie('csrftoken');
        const request_change = new Request(
            urlServer + "jugadores/",
            {
            method: 'POST',
            body: JSON.stringify( {accion: "change_seguir",user:name } ),
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin' // Do not send CSRF token to another domain.
            }
        );
        
        const resp2 = await fetch(request_change)
        const respuesta2 = await resp2.json()    
    })

    return lic
}


rellenarLista = async (ini,fin)=>{
    let urlServer = "http://127.0.0.1:8000/";
    let csrftoken = getCookie('csrftoken');
    const request_rellenarLista = new Request(
        urlServer + "jugadores/",
        {
        method: 'POST',
        body: JSON.stringify( {accion: "rellenarLista"} ),
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin' // Do not send CSRF token to another domain.
        }
    );
    const resp1 = await fetch(request_rellenarLista)
    const respuesta1 = await resp1.json()

    lista_jugadores.innerHTML = '';   // se vacia la lista   
    lista_jugadores.appendChild(crear_cabecera()); // se pone la cabecera
    
    let cont = 0;
    respuesta1.lista_jugadores.forEach(element => {
        let nuevo = crear_jugador(element[0],element[2])
        if (cont%2) nuevo.style.backgroundColor = "rgb(155, 159, 163)";
        cont+=1

        lista_jugadores.appendChild( nuevo )
    });
    return respuesta1;
}





formulario.addEventListener('submit', async (evento)=>{
    evento.preventDefault();

    if (busqueda.value == ""){
        rellenarLista(0,10)
        cancelar_busqueda.style.display = "none";
        return;
    }
    let urlServer = "http://127.0.0.1:8000/";
    let csrftoken = getCookie('csrftoken');
    
    const request_search = new Request(
        urlServer + "jugadores/",
        {
        method: 'POST',
        body: JSON.stringify( {accion: "search" , cadena:busqueda.value} ),
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin' // Do not send CSRF token to another domain.
        }
    );

    const resp = await fetch(request_search)
    const respuesta = await resp.json()

    cancelar_busqueda.style.display = "inline-block";

    
    if  (!respuesta["error"]){
        console.log("ok")
        lista_jugadores.innerHTML = ''
        lista_jugadores.appendChild(crear_cabecera())
        lista_jugadores.appendChild(crear_jugador(respuesta['user'][0], respuesta['user'][2]))  
    }else{
        lista_jugadores.innerHTML = ''
    }
    
})


cancelar_busqueda.addEventListener('click', ()=>{
    rellenarLista(0,10);
    busqueda.value = "";
    cancelar_busqueda.style.display = "none";
})


rellenarLista(0,10);