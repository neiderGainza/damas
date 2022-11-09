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
    let span_nombre1 = document.createElement('span')
    let span_seguir1 = document.createElement('span')
   
    span_nombre1.innerText = 'Nombre';
    span_seguir1.innerText = 'Seguir';
   
    li_cabecera.style.backgroundColor = "gray";

    li_cabecera.appendChild(span_nombre1)
    li_cabecera.appendChild(span_seguir1)

    return li_cabecera
}


const crear_jugador = (name,val) =>{
    let li = document.createElement('li')
    let nombre = document.createElement('span')
    let span   = document.createElement('span')
    let toggle = document.createElement('form')
    let input = document.createElement('input')

    toggle.classList.add("main_jugadores-item-toggle")
    toggle.action = "#"
    toggle.method = "post"
    input.type = "checkbox";
    if (val){ input.click() }

    toggle.appendChild(input)
    toggle.appendChild(span)


    nombre.innerText = name
    li.appendChild(nombre)
    li.appendChild(toggle)


    span.addEventListener("click", ()=>{ input.click();})

    return li
}


rellenarLista = async (ini,fin)=>{
    let urlServer = "http://127.0.0.1:8000/"
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
    const resp = await fetch(request_rellenarLista)
    const respuesta = await resp.json()

    lista_jugadores.innerHTML = '';   // se vacia la lista   
    lista_jugadores.appendChild(crear_cabecera()); // se pone la cabecera
    
    let cont = 0;
    respuesta.lista_jugadores.forEach(element => {
        let nuevo = crear_jugador(element[0],element[3])
        if (cont%2) nuevo.style.backgroundColor = "rgb(155, 159, 163)";
        cont+=1

        lista_jugadores.appendChild( nuevo )
    });
    return respuesta;
}





formulario.addEventListener('submit', async (evento)=>{
    evento.preventDefault();

    if (busqueda.value == ""){
        rellenarLista(0,10)
        cancelar_busqueda.style.display = "none";
        return;
    }

    let urlServer = "http://127.0.0.1:8000/"
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
        lista_jugadores.appendChild(crear_jugador(respuesta['user'][0], respuesta['user'][3]))  
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