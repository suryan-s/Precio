import { useLocalStorage } from "usehooks-ts"
import { useEffect } from "react"
import { useLocation } from "wouter"
import {Button} from "@/components/ui/button"
export default function Home() {
    const [token, setToken] = useLocalStorage<string|null>("token", null)
    const [__, setLocation] = useLocation()

    useEffect(() => {
        if (token === null) {
            setLocation("/Login")
        }
    }, [token])
    return (
        <div className="flex flex-col space-y-2 text-center">
            <h1 className="text-2xl font-semibold tracking-tight">
                Welcome to the dashboard!
            </h1>
            <p className="text-sm text-muted-foreground">
                This is the dashboard. You can do stuff here.
            </p>
            <Button onClick={()=>{setToken(null)}}>Log Out</Button>
        </div>
    )
}