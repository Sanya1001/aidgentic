import { BellRing, Check } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Switch } from "@/components/ui/switch"

const notifications = [
  {
    title: "Your response has been requested.",
    description: "1 min ago",
  },
  {
    title: "You have a new message!",
    description: "1 min ago",
  },
  {
    title: "Crisis alert in New Mexico, California.",
    description: "5 mins ago",
  },
]

type CardProps = React.ComponentProps<typeof Card>

export function NotifCard({ className, ...props }: CardProps) {

  const handleRefresh = async () => {
    try {
      const response = await fetch("http://localhost:8000/invoke", {
        method: "POST",
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      // Handle success or other logic
      console.log("Refresh successful");
    } catch (error) {
      console.error("Error refreshing data:", error);
      // Handle error scenarios
    }
  };

  return (
    <Card className={cn("w-[380px]", className)} {...props} id="notif-card">
      <CardHeader>
        <CardTitle>Notifications</CardTitle>
        <CardDescription>You have 3 unread messages.</CardDescription>
      </CardHeader>
      <CardContent className="grid gap-4">
        <div className=" flex items-center space-x-4 rounded-md border p-4">
          <BellRing />
          <div className="flex-1 space-y-1">
            <p className="text-sm font-medium leading-none">
              Email Notifications
            </p>
            <p className="text-sm text-muted-foreground">
              Send notifications to device.
            </p>
          </div>
          <Switch />
        </div>
        <div>
          {notifications.map((notification, index) => (
            <div
              key={index}
              className="mb-4 grid grid-cols-[25px_1fr] items-start pb-4 last:mb-0 last:pb-0"
            >
              <span className="flex h-2 w-2 translate-y-1 rounded-full bg-sky-500" />
              <div className="space-y-1">
                <p className="text-sm font-medium leading-none">
                  {notification.title}
                </p>
                <p className="text-sm text-muted-foreground">
                  {notification.description}
                </p>
              </div>
            </div>
          ))}
        </div>
      </CardContent>
      <CardFooter id="refresh">
        <Button className="w-full">
          <Check className="mr-2 h-4 w-4" /> Mark all as read
        </Button>
        <Button className="w-full" onClick={handleRefresh} id="refresh-button">ReSync</Button>
      </CardFooter>
    </Card>
  )
}
