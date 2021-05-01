import {
  SubscribeMessage,
  WebSocketGateway,
  OnGatewayInit,
  WebSocketServer,
  OnGatewayConnection,
  OnGatewayDisconnect,
} from '@nestjs/websockets';
import { Logger } from '@nestjs/common';
import { cpu, mem } from 'node-os-utils';
import { Socket, Server } from 'socket.io';

@WebSocketGateway()
export class SocketGateway
  implements OnGatewayInit, OnGatewayConnection, OnGatewayDisconnect {
  @WebSocketServer() server: Server;
  // Create a new logger for the gateway
  private logger: Logger = new Logger('SocketGateway');

  // Logging status
  afterInit() {
    this.logger.log('Init');
  }

  handleDisconnect(client: Socket) {
    this.logger.log(`Client disconnected: ${client.id}`);
  }

  handleConnection(client: Socket) {
    this.logger.log(`Client connected: ${client.id}`);
    // Send the first info
    this.handleConfig(client);
    this.handleUsage(client);
  }

  // ** Message handlers **

  // Message with the server configuration and status
  @SubscribeMessage('assistant.config.req')
  handleConfig(client: Socket): void {
    // TODO Manage this data
    client.emit('assistant.config.res', ['http://127.0.0.1', '', false, false]);
  }
  // Message with the device usage
  @SubscribeMessage('device.usage.req')
  async handleUsage(client: Socket): Promise<void> {
    const cpuUsage = await cpu.usage();
    const memUsage = await mem.info();
    client.emit('device.usage.res', [
      cpuUsage,
      (memUsage.usedMemMb / memUsage.totalMemMb) * 100,
    ]);
  }
}
