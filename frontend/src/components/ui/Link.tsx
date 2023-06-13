import { useLocation } from "wouter";

/**
 * Link component for hash-based routing
 */
export function Link({ className, href, children, ...props }: any) {
    const [_, setLocation] = useLocation();
    return (
        <a
        href={"#" + href}
        className={className}
        onClick={(e) => {
            e.preventDefault();
            setLocation(href);
        }}
        {...props}
        >
        {children}
        </a>
    );
}