import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { SocketIoAdapter } from './Socket/socket.adapter';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  // Appling adapter to used until Nest use SocketIO v.3
  app.useWebSocketAdapter(new SocketIoAdapter(app, true));
  await app.listen(4000);
}
bootstrap();
