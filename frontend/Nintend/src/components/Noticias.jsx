export default function Card({ image, title, description }) {
    return (
      <div className="bg-white rounded-2xl shadow-lg overflow-hidden h-full hover:shadow-xl transition-all duration-300 hover:scale-105 transform">
        <img src={image} alt={title} className="w-full h-48 object-cover" />
        <div className="p-4">
          <h2 className="text-xl font-semibold mb-2">{title}</h2>
          <p className="text-gray-600">{description}</p>
        </div>
      </div>
    )
  }