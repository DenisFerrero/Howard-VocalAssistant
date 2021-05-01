import { Module } from '@nestjs/common';
import { SocketGateway } from './Socket/socket.gateway';

@Module({
  imports: [],
  controllers: [],
  providers: [SocketGateway],
})
export class AppModule {}
