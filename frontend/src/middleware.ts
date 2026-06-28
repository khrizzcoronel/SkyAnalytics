import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const path = request.nextUrl.pathname;
  // Solo proteger las rutas del módulo estratégico
  if (
    path.startsWith('/api/v1/estrategico') || 
    path.startsWith('/dashboard/bsc') || 
    path.startsWith('/dashboard/finance') || 
    path.startsWith('/dashboard/engineering')
  ) {
    
    // Aquí normalmente validaríamos el JWT (PocketBase token)
    const token = request.headers.get('Authorization') || request.cookies.get('pb_auth')?.value;
    
    if (!token) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    // Mock de verificación para simular el comportamiento esperado
    const isOperator = token.includes('operator-token');
    if (isOperator) {
      return NextResponse.json(
        { error: 'Forbidden: Insufficient permissions' },
        { status: 403 }
      );
    }

    // Permitir acceso a BOARD_MEMBER para finanzas/ingenieria
    return NextResponse.next();
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    '/api/v1/estrategico/:path*',
    '/dashboard/bsc/:path*',
    '/dashboard/finance/:path*',
    '/dashboard/engineering/:path*'
  ],
};
