function getGamepadInfo()
{   
    gp_object = navigator.getGamepads()[0]
    for(let i = 0;i<gp_object.buttons.length;i++)
    {
        if(gp_object.buttons[i].value === 1)
        {
            botonPresionado = `$OAXBTN${i}`
            fetch(`/devTumi/gamepadButton?comando=${botonPresionado}`)
            .then(response => response.json())
            .then(data => {
                if(data.mensaje === 'recibido')
                {
                    elemento_html = document.getElementById(String(i))
                    elemento_html.value = '0'
                    elemento_html.value = '1'
                }
            })
            
        }
    }
    elementos_html = document.getElementsByClassName('botones')
    Array.from(elementos_html).forEach( elemento => {
        elemento.value = '0'
    })
}
let infoGamepad = null

document.addEventListener('DOMContentLoaded',()=>{
    window.addEventListener("gamepadconnected", function(e) {
        console.log('Gamepad ha sido conectado')
        infoGamepad = setInterval(getGamepadInfo,100)
    })

    window.addEventListener("gamepaddisconnected", function(e) {
        console.log('Gamepad ha sido desconectado')
        clearInterval(infoGamepad)
    })
})