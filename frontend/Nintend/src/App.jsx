import { useState } from 'react'
import Topbar from './components/topbar.jsx'
import HorizontalScroll from './components/ScrollHorizontal.jsx' // Changed import name to match component
import ns2Desktop from './assets/ns2-desktop.avif'
import ns2Mobile from './assets/ns2-mobile.avif'
import consoles from './assets/switch-family-es.avif'

function App() {
  // Arreglo de cartas de prueba
  const noticias = [
    {
      image: ns2Desktop,
      title: "Nintendo Switch 2",
      description: "La nueva consola de Nintendo con mejor rendimiento, resolución 4K y retrocompatibilidad.",
    },
    {
      image: ns2Desktop,
      title: "Zelda Returns",
      description: "Una nueva entrega de la saga de Zelda ha sido anunciada para la próxima generación.",
    },
    {
      image: ns2Desktop,
      title: "Mario Kart Ultimate",
      description: "Todos los circuitos y personajes en una sola edición definitiva.",
    },
    {
      image: ns2Desktop,
      title: "Metroid Prime 5",
      description: "Samus regresa con una historia épica y gráficos de nueva generación.",
    },
    {
      image: ns2Desktop,
      title: "Pokémon Eclipse",
      description: "La nueva generación de Pokémon con una región completamente nueva.",
    },
    {
      image: ns2Desktop,
      title: "Pokémon Eclipse",
      description: "La nueva generación de Pokémon con una región completamente nueva.",
    },
    {
      image: ns2Desktop,
      title: "Pokémon Eclipse",
      description: "La nueva generación de Pokémon con una región completamente nueva.",
    },
    {
      image: ns2Desktop,
      title: "Pokémon Eclipse",
      description: "La nueva generación de Pokémon con una región completamente nueva.",
    },

  ]

  return (
    <div className="App">
      <Topbar />
      <div className="container mx-auto px-4">
        <h1 className="text-3xl font-bold text-center mt-10">Welcome to Nintendo</h1>

        {/* Imagen responsive */}
        <img src={ns2Desktop} alt="Nintendo Switch 2 Desktop" className="rounded-2xl hidden md:block w-full mt-10" />
        <img src={ns2Mobile} alt="Nintendo Switch 2 Mobile" className="rounded-2xl block md:hidden w-full mt-10" />
        <div className='mt-10 flex flex-row items-center'> 
          <p className="font-bold mr-5 text-2xl"> Descubre las nuevas capacidades del Nintendo Switch 2</p>
          <button type='button'
            className="bg-[#e60012] text-white rounded-2xl pt-2.5 pb-2.5 p-5 hover:bg-red-700 transition duration-300"
            onClick={() => window.location.href = ''}
          >
            Revisa aqui
          </button>
        </div>

        {/* Linea divisora */}
        <div className="w-full border-t border-gray-300 mt-10 mb-10"></div>

        <h2 className="text-2xl font-bold text-left">Últimas Noticias</h2>
        <div className="mt-5">
          <HorizontalScroll noticias={noticias} />
        </div>

        {/* Linea divisora */}
        <div className="w-full border-t border-gray-300 mt-10 mb-10"></div>

        <h2 className="text-2xl font-bold text-left"> Tienda de consolas</h2>
        <img src={consoles} 
          alt="consolas vendidas"
          className="rounded-2xl mt-5"
        />
        <button type='button'
            className="bg-[#e60012] justify-center mt-5 text-white rounded-2xl pt-2.5 pb-2.5 p-5 hover:bg-red-700 transition duration-300"
            onClick={() => window.location.href = ''}
          >
            Compra las consolas aqui
          </button>
      </div>

      <div className="w-full border-t border-gray-300 mt-10 mb-10"></div>
    </div>
  )
}

export default App