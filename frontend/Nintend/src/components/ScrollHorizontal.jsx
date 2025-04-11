import React, { useRef } from 'react'
import Noticias from './Noticias.jsx'

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
      {/* Gradiente izquierdo - efecto de desvanecimiento */}
      <div className="absolute left-0 top-0 bottom-0 w-16 z-10 pointer-events-none" 
           style={{
             background: 'linear-gradient(90deg, rgba(255,255,255,1) 0%, rgba(255,255,255,0) 100%)'
           }}>
      </div>
      
      {/* Botones para desplazarse hacia la izquierda y derecha */}
      <button
        onClick={handleScrollLeft}
        className="absolute left-0 top-1/2 transform -translate-y-1/2 bg-[#e60012] text-white p-2 rounded-full z-20"
      >
        &lt;
      </button>
      
      {/* Contenedor con scroll horizontal */}
      <div 
        className="flex overflow-x-auto gap-6 p-4 scrollbar-hide" 
        ref={scrollContainer}
        style={{
          scrollbarWidth: 'none',  /* Firefox */
          msOverflowStyle: 'none',  /* IE and Edge */
          WebkitOverflowScrolling: 'touch'
        }}
      >
        {/* Mapeamos las cartas y las renderizamos */}
        {noticias.map((noticia, index) => (
          <div key={index} className="flex-shrink-0" style={{ width: '280px' }}>
            <Noticias
              image={noticia.image}
              title={noticia.title}
              description={noticia.description}
            />
          </div>
        ))}
      </div>
      
      {/* Gradiente derecho - efecto de desvanecimiento */}
      <div className="absolute right-0 top-0 bottom-0 w-16 z-10 pointer-events-none" 
           style={{
             background: 'linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(255,255,255,0) 100%)'
           }}>
      </div>
      
      {/* Botón para desplazarse hacia la derecha */}
      <button
        onClick={handleScrollRight}
        className="absolute right-0 top-1/2 transform -translate-y-1/2 bg-[#e60012] text-white p-2 rounded-full z-20"
      >
        &gt;
      </button>
    </div>
  )
}