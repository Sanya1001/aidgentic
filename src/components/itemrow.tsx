import * as React from "react"

import { Card, CardContent } from "@/components/ui/card"
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel"

const items = [
    {
        title: "FirstAid",
        quantity: "$1 M.",
    },
    {
        title: "Medicines",
        quantity: "$1 M.",
    },
    {
        title: "Food",
        quantity: "$1 M.",
    },
    {
        title: "Water",
        quantity: "2 tonnes",
    },
    {
        title: "Volunteers",
        quantity: "20",
    },
    {
        title: "Safety Kit",
        quantity: "15 sets",
    },

]

export function CarouselSize() {
  return (
    <Carousel
      opts={{
        align: "start",
      }}
      className="w-full"
    >
      <CarouselContent className="w-full">
        {items.map((item, index) => (
          <CarouselItem key={index} className="md:basis-1/2 lg:basis-1/5">
            <div className="p-1">
              <Card className="car-content">
                <CardContent className="flex flex-col aspect-square items-center justify-center p-6 car-content">
                    <span className="text-3xl font-semibold">{item.title}</span>
                    <br />
                  <span className="text-3xl font-semibold">{item.quantity}</span>
                </CardContent>
              </Card>
            </div>
          </CarouselItem>
        ))}
      </CarouselContent>
      <CarouselPrevious />
      <CarouselNext />
    </Carousel>
  )
}
