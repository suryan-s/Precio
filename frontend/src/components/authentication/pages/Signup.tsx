import { SignupForm } from "@/components/authentication/UserAuthForms"
import PrettyWrapper from "@/components/authentication/PrettyWrapper"
export default function Signup() {
    return (
        <PrettyWrapper>
            <div className="flex flex-col space-y-2 text-center">
              <h1 className="text-2xl font-semibold tracking-tight">
                Create an account
              </h1>
              <p className="text-sm text-muted-foreground">
                Enter your details below to create your account.
              </p>
            </div>
            <SignupForm />
        </PrettyWrapper>
    )
}