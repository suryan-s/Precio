import { LoginForm } from "@/components/authentication/UserAuthForms"
import PrettyWrapper from "@/components/authentication/PrettyWrapper"
export default function Login() {
    return (
        <PrettyWrapper>
            <div className="flex flex-col space-y-2 text-center">
              <h1 className="text-2xl font-semibold tracking-tight">
                Log In
              </h1>
              <p className="text-sm text-muted-foreground">
                Welcome back! Enter your email and password to log in!
              </p>
            </div>
            <LoginForm />
        </PrettyWrapper>
    )
}