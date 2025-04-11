import React, { useRef } from 'react'
import Noticias from './Noticias.jsx' // Asegúrate de tener el componente Noticias

export default function HorizontalScroll({ noticias }) {
  const scrollContainer = useRef(null)

  // Función para hacer scroll hacia la derecha
  const handleScrollRight = () => {
    if (scrollContainer.current) {
      scrollContainer.current.scrollBy({ left: 300, behavior: 'smooth' })
    }
  }

  // Función para hacer scroll hacia la izquierda
  const handleScrollLeft = () => {
    if (scrollContainer.current) {
      scrollContainer.current.scrollBy({ left: -300, behavior: 'smooth' })
    }
  }

  return (
    <div className="relative">
      {/* Botones para desplazarse hacia la izquierda y derecha */}
      <button 
        onClick={handleScrollLeft} 
        className="absolute left-0 top-1/2 transform -translate-y-1/2 bg-gray-700 text-white p-2 rounded-full"
      >
        &lt;
      </button>

      {/* Contenedor con scroll horizontal */}
      <div className="flex overflow-x-auto gap-6 p-4" ref={scrollContainer}>
        {/* Mapeamos las cartas y las renderizamos */}
        {noticias.map((noticia, index) => (
          <Noticias
            key={index}
            image={noticia.image}
            title={noticia.title}
            description={noticia.description}
          />
        ))}
      </div>

      {/* Botón para desplazarse hacia la derecha */}
      <button 
        onClick={handleScrollRight} 
        className="absolute right-0 top-1/2 transform -translate-y-1/2 bg-gray-700 text-white p-2 rounded-full"
      >
        &gt;
      </button>
    </div>
  )
}
